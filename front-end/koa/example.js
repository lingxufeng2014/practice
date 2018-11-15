let Koa = require('./lib/application');
let app = new Koa();

const responseData = {};
app.use(async (ctx, next) => {
    responseData.name = 'tom';
    await next();
    ctx.body = responseData;
});

app.use(async (ctx, next) => {
    responseData.age = 16;
    await next();
});

app.use(async (ctx) => {
    responseData.sex = 'male';
    throw new Error('error message');
});

app.listen(3000, () => {
    console.log('listening on 3000');
});
