'use strict'

class StopListCtrl
  @$inject: ['$scope', 'api.services.stops']
  constructor: (@$scope, @stpsvc) ->
    # console.log(@$scope)
    @$scope.stops = stpsvc.get({page:1, page_size:100})
    @$scope.stops.$promise.then (d) =>
      @$scope.stops = d
      angular.forEach @$scope.stops.data, (s) ->
        L.marker(s.attributes.pos.coordinates, {icon: blueIcon}).bindPopup(s.attributes.name).addTo(map)

angular.module('TransiteApp').controller 'StopListCtrl', StopListCtrl
