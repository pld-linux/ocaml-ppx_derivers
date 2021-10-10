#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Shared deriving plugin registry for OCaml
Summary(pl.UTF-8):	Współdzielony rejestr wtyczek wywodzących dla OCamla
Name:		ocaml-ppx_derivers
Version:	1.2.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/ocaml-ppx/ppx_derivers/releases
Source0:	https://github.com/ocaml-ppx/ppx_derivers/archive/%{version}/ppx_derivers-%{version}.tar.gz
# Source0-md5:	5dc2bf130c1db3c731fe0fffc5648b41
URL:		https://github.com/ocaml-ppx/ppx_derivers
BuildRequires:	ocaml >= 1:4.00
BuildRequires:	ocaml-dune
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Ppx_derivers is a tiny package whose sole purpose is to allow
ppx_deriving and ppx_type_conv to inter-operate gracefully when linked
as part of the same ocaml-migrate-parsetree driver.

This package contains files needed to run bytecode executables using
ppx_derivers library.

%description -l pl.UTF-8
Ppx_derivers to mały pakiet, którego jedynym celem jest umożliwienie
pakietom ppx_deriving oraz ppx_type_conv dobrej współpracy przy
włączeniu jako części tego samego sterownika ocaml-migrate-parsetree.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_derivers.

%package devel
Summary:	Shared deriving plugin registry for OCaml - development part
Summary(pl.UTF-8):	Współdzielony rejestr wtyczek wywodzących dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
ppx_derivers library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki ppx_derivers.

%prep
%setup -q -n ppx_derivers-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_derivers/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_derivers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_derivers
%{_libdir}/ocaml/ppx_derivers/META
%{_libdir}/ocaml/ppx_derivers/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_derivers/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_derivers/*.cmi
%{_libdir}/ocaml/ppx_derivers/*.cmt
%{_libdir}/ocaml/ppx_derivers/*.cmti
%{_libdir}/ocaml/ppx_derivers/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_derivers/*.a
%{_libdir}/ocaml/ppx_derivers/*.cmx
%{_libdir}/ocaml/ppx_derivers/*.cmxa
%endif
%{_libdir}/ocaml/ppx_derivers/dune-package
%{_libdir}/ocaml/ppx_derivers/opam
