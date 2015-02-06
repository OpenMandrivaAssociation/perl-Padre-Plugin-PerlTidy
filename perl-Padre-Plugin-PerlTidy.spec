%define upstream_name    Padre-Plugin-PerlTidy
%define upstream_version 0.22

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Format perl files using Perl::Tidy
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-PerlTidy-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Perl::Tidy)
BuildRequires:	perl(Test::More)
BuildRequires:	x11-server-xvfb
BuildArch:	noarch

%description
This is a simple plugin to run Perl::Tidy on your source code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
xvfb-run perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# no testing, wx fails with missing display
#%make test

%install
%makeinstall_std

%files
%doc Changes 
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 656956
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 622999
- new version

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.100.0-2mdv2011.0
+ Revision: 614530
- the mass rebuild of 2010.1 packages

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 494934
- update to 0.10

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 491631
- update to 0.09

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 418153
- adding missing buildrequires:
- update to 0.08

* Thu Jun 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 386971
- update to 0.07
- using %%perl_convert_version
- fix license tag

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2010.0
+ Revision: 378235
- update to new version 0.06

* Mon May 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-2mdv2010.0
+ Revision: 371828
- bumping mkrel to force re-submission

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.05-1mdv2010.0
+ Revision: 369800
- update to new version 0.05

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.02-1mdv2009.1
+ Revision: 328976
- removing testing, wx fails with missing display
- import perl-Padre-Plugin-PerlTidy


* Tue Jan 13 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist


