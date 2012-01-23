#!/bin/sh

URL="https://gigi.svn.sourceforge.net/svnroot/gigi/trunk/GG"
NAME=libgigi
SVN_REV=1044
VERSION=0.8.0


svn export -r ${SVN_REV} ${URL} ${NAME}-${VERSION}
tar -czvf ${NAME}-${VERSION}.tar.gz ${NAME}-${VERSION}/
rm -rf ${NAME}-${VERSION}
