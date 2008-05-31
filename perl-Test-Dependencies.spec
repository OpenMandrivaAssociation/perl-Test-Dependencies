%define module   Test-Dependencies
%define version    0.11
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Ensure that your Makefile.PL specifies all module dependencies
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
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
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Makes sure that all of the modules that are 'use'd are listed in the
Makefile.PL as dependencies.

%prep
%setup -q -n %{module}-%{version} 

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

