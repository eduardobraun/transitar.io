'use strict'

class StopListCtrl
  @$inject: ['$scope', 'api.services.stops']
  constructor: (@$scope, @stpsvc) ->
    # console.log(@$scope)
    @stops = [{name: "Stop 1"}
              {name: "Stop 2"}]
    stpsvc.all().then (d) =>
      @stops = d
      angular.forEach @stops, (s) ->
        L.marker(s.attributes.pos.coordinates, {icon: blueIcon}).bindPopup(s.attributes.name).addTo(map)

angular.module('TransiteApp').controller 'StopListCtrl', StopListCtrl
