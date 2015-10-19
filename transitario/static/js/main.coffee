transite_modules = [
  'TransiteAPIService'
  'StopListCtrl'
]

m = angular.module('TransiteApp', [])
m.config ($interpolateProvider) ->
      $interpolateProvider.startSymbol('{[{')
      $interpolateProvider.endSymbol('}]}')
