'use strict'

class TransiteAPIService
  @$inject: ['$http', '$log']
  @base_url: 'https://transite.me'
  constructor: (@$http, $log) ->
    $log.debug 'TransiteAPIService instance'
  stops: ->
    @$http.get("#{base_url}/api/stops")

angular.module('TransiteApp').service 'TransiteAPIService', TransiteAPIService

