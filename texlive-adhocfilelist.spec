# revision 29349
# category Package
# catalog-ctan /support/adhocfilelist
# catalog-date 2013-01-04 14:33:54 +0100
# catalog-license lppl
# catalog-version 2013-01-04
Name:		texlive-adhocfilelist
Version:	20130104
Release:	4
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
Provides:	texlive-adhocfilelist.bin = %{EVRD}

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
%{_bindir}/adhocfilelist
%{_texmfdistdir}/scripts/adhocfilelist/adhocfilelist.sh
%{_texmfdistdir}/scripts/adhocfilelist/herelist.sh
%{_texmfdistdir}/tex/support/adhocfilelist/adhocfilelist.RLS
%doc %{_texmfdistdir}/doc/support/adhocfilelist/README
%doc %{_texmfdistdir}/doc/support/adhocfilelist/RELEASEs.txt
%doc %{_texmfdistdir}/doc/support/adhocfilelist/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/support/adhocfilelist/adhocfilelist.htm
%doc %{_texmfdistdir}/doc/support/adhocfilelist/demo/herelist.txt
#- source
%doc %{_texmfdistdir}/source/support/adhocfilelist/adhocfilelist.tex
%doc %{_texmfdistdir}/source/support/adhocfilelist/fdatechk.tex
%doc %{_texmfdistdir}/source/support/adhocfilelist/makehtml.tex
%doc %{_texmfdistdir}/source/support/adhocfilelist/srcfiles.tex
%doc %{_texmfdistdir}/source/support/adhocfilelist/texblog.fdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/adhocfilelist/adhocfilelist.sh adhocfilelist
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
