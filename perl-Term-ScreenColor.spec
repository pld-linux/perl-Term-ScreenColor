#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define pnam	ScreenColor
Summary:	Term::ScreenColor - screen positioning and coloring module for Perl
Summary(pl):	Term::ScreenColor - modu³ pozycjonowania i kolorowania ekranu dla Perla
Name:		perl-Term-ScreenColor
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a0f26e057b1fd526f16362385ca1623
BuildRequires:	perl-Term-Screen
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ScreenColor adds ANSI coloring support, along with a few other
useful methods, to the objects provided in Term::Screen.

%description -l pl
Term::ScreenColor dodaje obs³ugê kolorów ANSI oraz parê innych
u¿ytecznych metod do obiektów dostarczonych w module Term::Screen.

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
