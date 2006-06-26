#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Graph - graph operations
Summary(pl):	Graph - operacje na grafach
Name:		perl-Graph
Version:	0.75
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graph/Graph-%{version}.tar.gz
# Source0-md5:	82cd9b9ffda237b1d278a3189eb0f824
BuildRequires:	perl-Heap >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph - graphs and graph algorithms. This is just a front-end class
for Graph::Directed and Graph::Base.

%description -l pl
Graph - grafy i algorytmy z nimi zwi±zane. Jest to po prostu klasa
zewnêtrzna dla Graph::Directed i Graph::Base.

%prep
%setup -q -n Graph-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Graph/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Graph.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Graph.pm
%{perl_vendorlib}/Graph/*
%{_mandir}/man3/*
