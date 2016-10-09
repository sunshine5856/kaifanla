/**
 * Created by sunshine on 2016/10/8.
 */
var app = angular.module('kaifanla', ['ng', 'ngRoute']);
app.controller('parentCtrl', function ($scope,$location) {
    $scope.jump = function (path) {
        $location.path(path);
    }
})
app.controller('startCtrl', function ($scope, $location) {
    /*  $scope.jump = function () {
     $location.path('/main');
     }*/
})
app.config(function ($routeProvider) {
    $routeProvider
        .when('/start', {
            templateUrl: 'templates/start.html',
            controller:'startCtrl'
        })
        .when('/main',{
            templateUrl:'templates/main.html'
        })
        .when('/detail',{
            templateUrl:'templates/detail.html'
        })
        .when('/order',{
            templateUrl:'templates/order.html'
        })
        .when('/myOrder',{
            templateUrl:'templates/myOrder.html'
        }).otherwise({redirectTo:'/start'});
})
