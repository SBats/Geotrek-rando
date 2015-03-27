'use strict';

var controllers = require('./controllers');

function homePage() {
    return {
        restrict: 'E',
        replace: true,
        scope: true,
        template: require('./templates/home-page.html'),
        controller: controllers.HomeController
    };
}

module.exports = {
    homePage: homePage
};