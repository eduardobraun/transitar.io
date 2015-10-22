'use strict'

# class Stops
#   @$inject: ['$resource', '$log']
#   url = "/api/stops/:id"
#   constructor:(@$resource, @$log) ->
#     return $resource url, {id: "@id"}, { update: {method: "PUT"} } 


# angular.module("TransiteApp").factory "Stops", Stops

base_name = 'api.services'

class Stops
  @$inject: ['$http', '$log', '$q']
  constructor: (@$http, @$log, @$q) ->
    @deferred = @$q.defer()
    @data = []

  _get_page: (p)->
    return @$http.get(p)

  _get_all_pages: (p) ->
    @_get_page(p).success (d) =>
      @data = @data.concat(d.data)
      # @$log.log(d.data)
      if d.links.next != null
        @_get_all_pages(d.links.next)
      else
        @deferred.resolve(@data)
    return @deferred.promise

  _get: (relPath)->
    return @$http.get("/api/stops#{relPath}")

  all: () ->
    @data = []
    return @_get_all_pages("/api/stops")

  one: (id) ->
    return @_get("/#{id}")

angular.module("#{base_name}.stops", []).service "#{base_name}.stops", Stops

