Name:		texlive-proba
Version:	15878
Release:	2
Summary:	Shortcuts commands to symbols used in probability texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proba
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package includes some of the most often used commands in
probability texts, e.g. probability, expectation, variance,
etc. It also includes some short commands for set (blackboard)
or filtrations (calligraphic). It requires LaTeX2e and the
amsfonts package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/proba/proba.sty
%doc %{_texmfdistdir}/doc/latex/proba/README
%doc %{_texmfdistdir}/doc/latex/proba/proba.pdf
#- source
%doc %{_texmfdistdir}/source/latex/proba/proba.dtx
%doc %{_texmfdistdir}/source/latex/proba/proba.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
