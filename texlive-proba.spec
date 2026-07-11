%global tl_name proba
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Shortcuts commands to symbols used in probability texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/proba
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/proba.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package includes some of the most often used commands in
probability texts, e.g. probability, expectation, variance, etc. It also
includes some short commands for set (blackboard) or filtrations
(calligraphic). It requires LaTeX2e and the amsfonts package.

