Name:		texlive-imac
Version:	17347
Release:	2
Summary:	International Modal Analysis Conference format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/imac
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of files for producing correctly formatted documents for
the International Modal Analysis Conference. The bundle
provides a LaTeX package and a BibTeX style file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/imac
%{_texmfdistdir}/tex/latex/imac
%doc %{_texmfdistdir}/doc/latex/imac

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
