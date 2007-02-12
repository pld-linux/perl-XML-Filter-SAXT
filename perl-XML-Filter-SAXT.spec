#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Filter-SAXT
Summary:	XML::Filter::SAXT - replicates SAX events to several SAX event handlers
Summary(pl.UTF-8):   XML::Filter::SAXT - powielanie zdarzeń SAX dla wielu funkcji obsługi zdarzeń SAX
Name:		perl-XML-Filter-SAXT
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	da65cbe1938bff4c8975014c80063e05
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAXT is like the Unix 'tee' command in that it multiplexes the input
stream to several output streams. In this case, the input stream is a
PerlSAX event producer (like XML::Parser::PerlSAX) and the output
streams are PerlSAX handlers or filters.

%description -l pl.UTF-8
SAXT jest modułem podobnym do uniksowego polecenia 'tee' pod tym
względem, że powiela strumień wejściowy na kilka strumieni
wyjściowych. W tym przypadku strumień wyjściowy to moduł tworzący
zdarzenia PerlSAX (jak XML::Parser::PerlSAX), a strumienie wyjściowe
są funkcjami obsługi lub filtrami PerlSAX.

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
%doc Changes README
%{perl_vendorlib}/XML/Filter/SAXT.pm
%{_mandir}/man3/*
