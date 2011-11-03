# revision 17347
# category Package
# catalog-ctan /macros/latex/contrib/imac
# catalog-date 2010-03-06 17:30:22 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-imac
Version:	20100306
Release:	1
Summary:	International Modal Analysis Conference format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/imac
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of files for producing correctly formatted documents for
the International Modal Analysis Conference. The bundle
provides a LaTeX package and a BibTeX style file.

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
%{_texmfdistdir}/bibtex/bst/imac/imac.bst
%{_texmfdistdir}/tex/latex/imac/imac.sty
%doc %{_texmfdistdir}/doc/latex/imac/imac.bib
%doc %{_texmfdistdir}/doc/latex/imac/imac.pdf
%doc %{_texmfdistdir}/doc/latex/imac/imac.tex
%doc %{_texmfdistdir}/doc/latex/imac/readme.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
