#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Graph perl module
Summary(pl):	Modu³ perla Graph
Name:		perl-Graph
Version:	0.20101
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graph/Graph-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Heap >= 0.01
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph - graphs and graph algorithms.

%description -l pl
Graph - grafy i algorytmy z nimi zwi±zane.

%prep
%setup -q -n Graph-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes DISCLAIMER
%{perl_vendorlib}/Graph.pm
%{perl_vendorlib}/Graph/*
%{_mandir}/man3/*
