transite_modules = [
  'ngResource'
  'ngRoute'
  'api.services.stops'
]

m = angular.module('TransiteApp', transite_modules)
m.config ($interpolateProvider) ->
      $interpolateProvider.startSymbol('{[{')
      $interpolateProvider.endSymbol('}]}')
