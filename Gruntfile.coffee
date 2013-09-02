module.exports = (grunt) ->

  # Project configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON('package.json')

    clean:
      src:
        ['generated/']

    coffee:
      src:
        files:
          'static/js/app.js': [
            'src/js/**/*.coffee'
          ]
        options:
          bare: true
          sourceMap: true

    ngmin:
      compile:
        files:
          'generated/js/app.ngmin.js': ['static/js/app.js']

    uglify:
      src:
        files:
          'static/js/app.min.js': ['generated/js/app.ngmin.js']
        options:
          mangle: true
          sourceMap: 'static/js/app.min.js.map'
          sourceMapIn: 'static/js/app.js.map'
          sourceMapRoot: '/js'
          sourceMappingURL: 'app.min.js.map'

    watch:
      scripts:
        files:
          ['src/**/*.coffee']
        tasks:
          ['default']
        options:
          livereload: true

  grunt.loadNpmTasks 'grunt-contrib-clean'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-uglify'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-ngmin'

  grunt.registerTask 'default', ['build', 'clean']
  grunt.registerTask 'build', ['coffee', 'ngmin', 'uglify']
