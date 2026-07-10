%global tl_name adhocfilelist
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	\listfiles entries from the command line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/adhocfilelist
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(adhocfilelist.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Unix shell script to display a list of LaTeX
\Provides...-command contexts on screen. Provision is made for
controlling the searches that the package does. The package was
developed on a Unix-like system, using (among other things) the gnu
variant of the find command.

