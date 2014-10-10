%define upstream_name    Test-Dependencies
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Ensure that your Makefile.PL specifies all module dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(B::PerlReq)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(PerlReq::Utils)
BuildRequires:	perl(Pod::Strip)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 466455
- update to 0.12

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 405548
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.11-2mdv2009.0
+ Revision: 268732
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
+ Revision: 213802
- import perl-Test-Dependencies


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2009.0
- first mdv release
