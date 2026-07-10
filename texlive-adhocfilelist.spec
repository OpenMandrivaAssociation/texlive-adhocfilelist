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
Requires(pre):	texlive-tlpkg
Requires:	texlive(adhocfilelist.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a Unix shell script to display a list of LaTeX
\Provides...-command contexts on screen. Provision is made for
controlling the searches that the package does. The package was
developed on a Unix-like system, using (among other things) the gnu
variant of the find command.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/source
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/adhocfilelist
%dir %{_datadir}/texmf-dist/texmf-dist/source/support
%dir %{_datadir}/texmf-dist/texmf-dist/tex/support
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist
%dir %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist
%dir %{_datadir}/texmf-dist/texmf-dist/tex/support/adhocfilelist
%dir %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/demo
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/RELEASEs.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/SrcFILEs.txt
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/adhocfilelist.htm
%doc %{_datadir}/texmf-dist/texmf-dist/doc/support/adhocfilelist/demo/herelist.txt
%{_datadir}/texmf-dist/texmf-dist/scripts/adhocfilelist/adhocfilelist.sh
%{_datadir}/texmf-dist/texmf-dist/scripts/adhocfilelist/herelist.sh
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist/adhocfilelist.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist/fdatechk.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist/makehtml.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist/srcfiles.tex
%doc %{_datadir}/texmf-dist/texmf-dist/source/support/adhocfilelist/texblog.fdf
%{_datadir}/texmf-dist/texmf-dist/tex/support/adhocfilelist/adhocfilelist.RLS
