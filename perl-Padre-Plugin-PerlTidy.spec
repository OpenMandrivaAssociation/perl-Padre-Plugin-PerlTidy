%define upstream_name    Padre-Plugin-PerlTidy
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Format perl files using Perl::Tidy
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Padre)
BuildRequires: perl(Perl::Tidy)
BuildRequires: perl(Test::More)
BuildRequires: x11-server-xvfb
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a simple plugin to run Perl::Tidy on your source code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
xvfb-run %{__perl} Build.PL installdirs=vendor
./Build

# no testing, wx fails with missing display
#%check
#./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
