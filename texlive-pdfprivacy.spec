Name:		texlive-pdfprivacy
Version:	45985
Release:	2
Summary:	A LaTeX package to remove or suppress pdf meta-data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfprivacy
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfprivacy.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Creating pdfs with pdfLaTeX populates several pdf meta-data
fields such as date/time of creation/modification, information
about the LaTeX installation (e.g., pdfTeX version), and the
relative paths of included pdfs. The pdfprivacy package
provides support for emptying several of these pdf meta-data
fields as well as suppressing some pdfTeX meta-data entries in
the resulting pdf.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/pdfprivacy
%{_texmfdistdir}/tex/latex/pdfprivacy
%doc %{_texmfdistdir}/doc/latex/pdfprivacy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
