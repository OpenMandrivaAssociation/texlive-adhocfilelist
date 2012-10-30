# revision 28038
# category Package
# catalog-ctan /support/adhocfilelist
# catalog-date 2012-10-20 17:13:23 +0200
# catalog-license lppl
# catalog-version 0.7a
Name:		texlive-adhocfilelist
Version:	0.7a
Release:	1
Summary:	'\listfiles' entries from the command line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/adhocfilelist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-adhocfilelist.bin

%description
The package provides a Unix shell script to display a list of
LaTeX \Provides...-command contexts on screen. Provision is
made for controlling the searches that the package does. The
package was developed on a Unix-like system, using (among other
things) the gnu variant of the find command.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/adhocfilelist/adhocfilelist.sh
%{_texmfdistdir}/scripts/adhocfilelist/herelist.sh
%doc %{_texmfdistdir}/doc/support/adhocfilelist/RELEASE.txt
%doc %{_texmfdistdir}/doc/support/adhocfilelist/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/support/adhocfilelist/adhocfilelist.htm
%doc %{_texmfdistdir}/doc/support/adhocfilelist/makehtml.log
#- source
%doc %{_texmfdistdir}/source/adhocfilelist/adhocfilelist.tex
%doc %{_texmfdistdir}/source/adhocfilelist/srcfiles.tex
%doc %{_texmfdistdir}/source/adhocfilelist/texblog.fdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
