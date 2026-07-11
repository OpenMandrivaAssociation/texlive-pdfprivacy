%global tl_name pdfprivacy
%global tl_revision 79126

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A LaTeX package to remove or suppress pdf meta-data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfprivacy
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Creating pdfs with pdfLaTeX populates several pdf meta-data fields such
as date/time of creation/modification, information about the LaTeX
installation (e.g., pdfTeX version), and the relative paths of included
pdfs. The pdfprivacy package provides support for emptying several of
these pdf meta-data fields as well as suppressing some pdfTeX meta-data
entries in the resulting pdf.

