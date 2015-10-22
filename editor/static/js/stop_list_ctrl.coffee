'use strict'

class StopListCtrl
  @$inject: ['$scope', 'api.services.stops']
  constructor: (@$scope, @stpsvc) ->
    # console.log(@$scope)
    @stops = [{name: "Stop 1"}
              {name: "Stop 2"}]

angular.module('TransiteApp').controller 'StopListCtrl', StopListCtrl
