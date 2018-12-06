#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Font-TTF
Version  : 1.06
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Font-TTF-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BH/BHALLISSY/Font-TTF-1.06.tar.gz
Summary  : 'TTF font support for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Font-TTF-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IO::String)

%description
=head1 INTRODUCTION
Perl module for TrueType/OpenType font hacking. Supports reading, processing and
writing of the following tables: GDEF, GPOS, GSUB, LTSH, OS/2, PCLT,
bsln, cmap, cvt, fdsc, feat, fpgm, glyf, hdmx, head, hhea, hmtx, kern,
loca, maxp, mort, name, post, prep, prop, vhea, vmtx and the reading and
writing of all other table types.

%package dev
Summary: dev components for the perl-Font-TTF package.
Group: Development
Provides: perl-Font-TTF-devel = %{version}-%{release}

%description dev
dev components for the perl-Font-TTF package.


%package license
Summary: license components for the perl-Font-TTF package.
Group: Default

%description license
license components for the perl-Font-TTF package.


%prep
%setup -q -n Font-TTF-1.06

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Font-TTF
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Font-TTF/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/AATKern.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/AATutils.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Anchor.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Bsln.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Changes_old.txt
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Cmap.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Coverage.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Cvt_.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/DSIG.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Delta.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/EBDT.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/EBLC.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Fdsc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Feat.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Features/Cvar.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Features/Size.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Features/Sset.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Fmtx.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Font.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Fpgm.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/GDEF.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/GPOS.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/GSUB.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Glat.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Gloc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Glyf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Glyph.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/GrFeat.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Hdmx.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Head.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Hhea.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Hmtx.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern/ClassArray.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern/CompactClassArray.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern/OrderedList.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern/StateTable.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Kern/Subtable.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/LTSH.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Loca.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Manual.pod
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Maxp.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Chain.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Contextual.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Insertion.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Ligature.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Noncontextual.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Rearrangement.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Mort/Subtable.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Name.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/OS_2.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/OTTags.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/OldCmap.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/OldMort.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/PCLT.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/PSNames.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Post.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Prep.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Prop.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Segarr.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Silf.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Sill.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Table.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Ttc.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Ttopen.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Useall.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Utils.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Vhea.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Vmtx.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Win32.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Woff.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Woff/MetaData.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/Woff/PrivateData.pm
/usr/lib/perl5/vendor_perl/5.28.1/Font/TTF/XMLparse.pm
/usr/lib/perl5/vendor_perl/5.28.1/ttfmod.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Font::TTF.3
/usr/share/man/man3/Font::TTF::AATKern.3
/usr/share/man/man3/Font::TTF::AATutils.3
/usr/share/man/man3/Font::TTF::Anchor.3
/usr/share/man/man3/Font::TTF::Bsln.3
/usr/share/man/man3/Font::TTF::Cmap.3
/usr/share/man/man3/Font::TTF::Coverage.3
/usr/share/man/man3/Font::TTF::Cvt_.3
/usr/share/man/man3/Font::TTF::DSIG.3
/usr/share/man/man3/Font::TTF::Delta.3
/usr/share/man/man3/Font::TTF::Dumper.3
/usr/share/man/man3/Font::TTF::EBDT.3
/usr/share/man/man3/Font::TTF::EBLC.3
/usr/share/man/man3/Font::TTF::Fdsc.3
/usr/share/man/man3/Font::TTF::Feat.3
/usr/share/man/man3/Font::TTF::Features::Cvar.3
/usr/share/man/man3/Font::TTF::Features::Size.3
/usr/share/man/man3/Font::TTF::Features::Sset.3
/usr/share/man/man3/Font::TTF::Fmtx.3
/usr/share/man/man3/Font::TTF::Font.3
/usr/share/man/man3/Font::TTF::Fpgm.3
/usr/share/man/man3/Font::TTF::GDEF.3
/usr/share/man/man3/Font::TTF::GPOS.3
/usr/share/man/man3/Font::TTF::GSUB.3
/usr/share/man/man3/Font::TTF::Glat.3
/usr/share/man/man3/Font::TTF::Gloc.3
/usr/share/man/man3/Font::TTF::Glyf.3
/usr/share/man/man3/Font::TTF::Glyph.3
/usr/share/man/man3/Font::TTF::GrFeat.3
/usr/share/man/man3/Font::TTF::Hdmx.3
/usr/share/man/man3/Font::TTF::Head.3
/usr/share/man/man3/Font::TTF::Hhea.3
/usr/share/man/man3/Font::TTF::Hmtx.3
/usr/share/man/man3/Font::TTF::Kern.3
/usr/share/man/man3/Font::TTF::Kern::ClassArray.3
/usr/share/man/man3/Font::TTF::Kern::CompactClassArray.3
/usr/share/man/man3/Font::TTF::Kern::OrderedList.3
/usr/share/man/man3/Font::TTF::Kern::StateTable.3
/usr/share/man/man3/Font::TTF::Kern::Subtable.3
/usr/share/man/man3/Font::TTF::LTSH.3
/usr/share/man/man3/Font::TTF::Loca.3
/usr/share/man/man3/Font::TTF::Manual.3
/usr/share/man/man3/Font::TTF::Maxp.3
/usr/share/man/man3/Font::TTF::Mort.3
/usr/share/man/man3/Font::TTF::Mort::Chain.3
/usr/share/man/man3/Font::TTF::Mort::Contextual.3
/usr/share/man/man3/Font::TTF::Mort::Insertion.3
/usr/share/man/man3/Font::TTF::Mort::Ligature.3
/usr/share/man/man3/Font::TTF::Mort::Noncontextual.3
/usr/share/man/man3/Font::TTF::Mort::Rearrangement.3
/usr/share/man/man3/Font::TTF::Mort::Subtable.3
/usr/share/man/man3/Font::TTF::Name.3
/usr/share/man/man3/Font::TTF::OS_2.3
/usr/share/man/man3/Font::TTF::OTTags.3
/usr/share/man/man3/Font::TTF::OldCmap.3
/usr/share/man/man3/Font::TTF::OldMort.3
/usr/share/man/man3/Font::TTF::PCLT.3
/usr/share/man/man3/Font::TTF::PSNames.3
/usr/share/man/man3/Font::TTF::Post.3
/usr/share/man/man3/Font::TTF::Prep.3
/usr/share/man/man3/Font::TTF::Prop.3
/usr/share/man/man3/Font::TTF::Segarr.3
/usr/share/man/man3/Font::TTF::Silf.3
/usr/share/man/man3/Font::TTF::Sill.3
/usr/share/man/man3/Font::TTF::Table.3
/usr/share/man/man3/Font::TTF::Ttc.3
/usr/share/man/man3/Font::TTF::Ttopen.3
/usr/share/man/man3/Font::TTF::Useall.3
/usr/share/man/man3/Font::TTF::Utils.3
/usr/share/man/man3/Font::TTF::Vhea.3
/usr/share/man/man3/Font::TTF::Vmtx.3
/usr/share/man/man3/Font::TTF::Win32.3
/usr/share/man/man3/Font::TTF::Woff.3
/usr/share/man/man3/Font::TTF::Woff::MetaData.3
/usr/share/man/man3/Font::TTF::Woff::PrivateData.3
/usr/share/man/man3/Font::TTF::XMLparse.3
/usr/share/man/man3/ttfmod.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Font-TTF/LICENSE
