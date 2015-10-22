
# Taken from https://github.com/roytruelove/angular-grunt-coffeescript/
providerName = 'common.services.env'
# angular adds the 'Provider' suffix for us.
modName = "#{providerName}Provider"

angular.module(modName, [])
  .provider(providerName, ()->
    throw new Error("Expecting this module to be overridden
      by an env specific version")
)

