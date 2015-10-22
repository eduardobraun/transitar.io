transite_modules = [
  'ngResource'
  'ngRoute'
  'api.services.stops'
  'common.services.envProvider'
  'StopListCtrl'
]

m = angular.module('TransiteApp', [])
m.config ($interpolateProvider) ->
      $interpolateProvider.startSymbol('{[{')
      $interpolateProvider.endSymbol('}]}')
