%define module Crypt-Random-Seed
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.03
Release:	1
Summary:	Simple method to get strong randomness
URL:		https://metacpan.org/pod/Crypt::Random::Seed
Source:		https://cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildArch:	noarch

%description
A simple mechanism to get strong randomness. The main purpose of this module is to provide a simple way to generate a seed for a PRNG such as Math::Random::ISAAC, for use in cryptographic key generation, or as the seed for an upstream module such as Bytes::Random::Secure. Flags for requiring non-blocking sources are allowed, as well as a very simple method for plugging in a source.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorlib}/*/*
%{_mandir}/man3/*.3pm*
