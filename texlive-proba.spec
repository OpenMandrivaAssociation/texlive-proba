Name:		texlive-proba
Version:	20090602
Release:	1
Summary:	Shortcuts commands to symbols used in probability texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proba
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package includes some of the most often used commands in
probability texts, e.g. probability, expectation, variance,
etc. It also includes some short commands for set (blackboard)
or filtrations (calligraphic). It requires LaTeX2e and the
amsfonts package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
