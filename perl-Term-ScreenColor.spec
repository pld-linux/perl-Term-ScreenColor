#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	ScreenColor
Summary:	Term::ScreenColor - screen positioning and coloring module for Perl
Summary(pl.UTF-8):	Term::ScreenColor - moduł pozycjonowania i kolorowania ekranu dla Perla
Name:		perl-Term-ScreenColor
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27a51f41c56d37cc12297844f28d597d
BuildRequires:	perl-Term-Screen
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ScreenColor adds ANSI coloring support, along with a few other
useful methods, to the objects provided in Term::Screen.

%description -l pl.UTF-8
Term::ScreenColor dodaje obsługę kolorów ANSI oraz parę innych
użytecznych metod do obiektów dostarczonych w module Term::Screen.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Term/ScreenColor.pm
%{_mandir}/man3/*
