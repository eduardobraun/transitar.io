transite_modules = [
  'ngResource'
  'ngRoute'
  'Stops'
  'TransiteAPIService'
  'StopListCtrl'
]

m = angular.module('TransiteApp', [])
m.config ($interpolateProvider) ->
      $interpolateProvider.startSymbol('{[{')
      $interpolateProvider.endSymbol('}]}')
