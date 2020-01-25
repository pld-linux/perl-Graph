#
# Conditional build:
%bcond_without	tests # do not perform "make test"

%define		pdir	Graph
Summary:	Graph - graph operations
Summary(pl.UTF-8):	Graph - operacje na grafach
Name:		perl-Graph
Version:	0.94
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Graph/Graph-%{version}.tar.gz
# Source0-md5:	21c7c5b108fdf898ca1679a0509ccbb2
URL:		http://search.cpan.org/dist/Graph/
BuildRequires:	perl-Heap >= 0.01
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph - graphs and graph algorithms. This is just a front-end class
for Graph::Directed and Graph::Base.

%description -l pl.UTF-8
Graph - grafy i algorytmy z nimi związane. Jest to po prostu klasa
zewnętrzna dla Graph::Directed i Graph::Base.

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
%dir %{perl_vendorlib}/Graph
%{perl_vendorlib}/Graph.pm
%{perl_vendorlib}/Graph/*
%{perl_vendorlib}/Heap071/
%{perl_vendorlib}/auto/Heap071/
%{_mandir}/man3/*
