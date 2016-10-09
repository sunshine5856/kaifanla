var gulp = require('gulp'), //本地安装gulp所用到的地方
    less = require('gulp-less');

//定义一个testLess任务（自定义任务名称）
gulp.task('testLess', function () {
    gulp.src('public/src/less/kaifanla.less') //该任务针对的文件
        .pipe(less()) //该任务调用的模块
        .pipe(gulp.dest('public/dist/css')); //将会在src/css下生成kaifanla.css
});

gulp.task('watch',function(){
    gulp.watch('/public/src/less/kaifanla.less',['testLess']);
});

gulp.task('default','watch')