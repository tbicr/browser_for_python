var gulp = require('gulp'),
    eslint = require('gulp-eslint'),
    qunit = require('gulp-qunit');

gulp.task('lint', function () {
    gulp.src('./tests.js')
        .pipe(eslint({
            rules:{
                'quotes': 'single'
            },
            globals: {
                'QUnit': true
            },
            env:{
                browser: true
            }
        }))
        .pipe(eslint.format());
});

gulp.task('test', function () {
    return gulp.src('./tests.html')
        .pipe(qunit());
});

gulp.task('default', function () {
    gulp.run('lint', 'test');
});
