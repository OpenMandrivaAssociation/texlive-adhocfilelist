Name:		texlive-adhocfilelist
Version:	29349
Release:	2
Summary:	'\listfiles' entries from the command line
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/adhocfilelist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adhocfilelist.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/adhocfilelist/adhocfilelist.sh adhocfilelist
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
