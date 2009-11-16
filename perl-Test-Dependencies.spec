%define upstream_name    Test-Dependencies
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Ensure that your Makefile.PL specifies all module dependencies
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::PerlReq)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(PerlReq::Utils)
BuildRequires: perl(Pod::Strip)
BuildRequires: perl(Test::Builder::Module)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(YAML)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Test
