%include	/usr/lib/rpm/macros.perl
Summary:	Graph perl module
Summary(pl):	Modu³ perla Graph
Name:		perl-Graph
Version:	0.201
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Graph/Graph-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Heap >= 0.01
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graph - graphs and graph algorithms.

%description -l pl
Graph - grafy i algorytmy z nimi zwi±zane.

%prep
%setup -q -n Graph-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Graph.pm
%{perl_sitelib}/Graph/*
%{_mandir}/man3/*
