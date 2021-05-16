//////////////////////////////////////////////////////////////////////////////
//                                                                          //
//  A library for making JavaScript environments LittleJ compatible.        //
//  Written purely in LittleJ (i.e Jispy's JavaScript subset).              //
//                                                                          //
//  Copyright (c) 2017 Polydojo, Inc.                                       //
//                                                                          //
//                                                                          //
//  This Source Code Form is subject to the terms of the Mozilla Public     //
//  License, v. 2.0. If a copy of the MPL was not distributed with this     //
//  file, You can obtain one at http://mozilla.org/MPL/2.0/.                //
//                                                                          //
//////////////////////////////////////////////////////////////////////////////


(function (context) {
    'use strict';
    context.keys = Object.keys;
    context.type = function (x) {
        if (x === null) { return 'null'; }
        if (Object.prototype.toString.call(x) === '[object Array]') { return 'array'; }
        return typeof x;
    };
    context.str = function (x) {
        if (typeof x === 'object') { return JSON.stringify(x); }
        return String(x);
    };
    context.print = function (x) {
        console.log(x);
        return null;
    };
    context.len = function (x) {
        if (context.type(x) === 'object') { return Object.keys(x).length; }
        return x.length;
    };
    context.del = function (x, y) {
        if (context.type(x) === 'array') {
            x.splice(y, 1);
            return true;
        }
        return delete x[y];
    };
    context.append = function (arr, elt) { arr.push(elt);  return context.len(arr); };
    context.assert = function (expr, msg) {
        if (expr) { return null; }
        throw new Error('AssertionError: ' + context.str(msg));
    };
    context.ord = function (c) { return c.charCodeAt(0); };
    context.chr = function (i) { return String.fromCharCode(i); };
    context.math = Math;
}(this));