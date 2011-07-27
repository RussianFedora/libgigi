#!/bin/sh

GG_NAME=libgigi
SVN_REV=1043

svn co -r ${SVN_REV} https://gigi.svn.sourceforge.net/svnroot/gigi/trunk gigi
cd gigi

# Get version of gigi
GG_VERSION=`cat GG/CMakeLists.txt | grep 'set(GIGI_VERSION' | awk '{print $2}' | sed 's|)||g'`
GG_FULL_NAME=${GG_NAME}-${GG_VERSION}

# Remove .svn
find . -name .svn -exec rm -rf {} \; > /dev/null

mv GG $GG_FULL_NAME
tar cfjv ../${GG_FULL_NAME}.tar.bz2 $GG_FULL_NAME
