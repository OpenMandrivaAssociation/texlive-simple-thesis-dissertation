Name:		texlive-simple-thesis-dissertation
Version:	43058
Release:	1
Summary:	Template for a simple thesis or dissertation (Ph.D. or master's degree) or technical report, in XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simple-thesis-dissertation
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-thesis-dissertation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-thesis-dissertation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Template for a simple thesis or dissertation (Ph.D. or master's
degree) or technical report, in XeLaTeX. Simple template that
can be further customized or extended, with numerous examples.
Consistent style for figures, tables, mathematical theorems,
definitions, lemmas, etc.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/simple-thesis-dissertation
%doc %{_texmfdistdir}/doc/xelatex/simple-thesis-dissertation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
