# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/proba
# catalog-date 2009-06-02 14:48:32 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-proba
Version:	20180303
Release:	3
Summary:	Shortcuts commands to symbols used in probability texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/proba
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090602-2
+ Revision: 755067
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090602-1
+ Revision: 719301
- texlive-proba
- texlive-proba
- texlive-proba
- texlive-proba
- texlive-proba

