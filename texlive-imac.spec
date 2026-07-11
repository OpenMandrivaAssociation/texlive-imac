%global tl_name imac
%global tl_revision 17347

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	International Modal Analysis Conference format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/imac
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/imac.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of files for producing correctly formatted documents for the
International Modal Analysis Conference. The bundle provides a LaTeX
package and a BibTeX style file.

