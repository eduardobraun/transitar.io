'use strict'

class StopListCtrl
  @$inject: ['$scope']
  constructor: (@$scope) ->
    # console.log(@$scope)
    @stops = [{name: "Stop 1"}
              {name: "Stop 2"}]

angular.module('TransiteApp').controller 'StopListCtrl', StopListCtrl
