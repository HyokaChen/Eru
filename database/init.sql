-- 全局配置模板表 --

CREATE TABLE public.configuration_global (
    id serial NOT NULL,
	start_url varchar NOT NULL,
	spider_name varchar NOT NULL,
	site_name varchar NOT NULL,
	request_method varchar NOT NULL DEFAULT 'GET',
	referer varchar NULL,
	need_render boolean NOT NULL DEFAULT false,
	timeout integer NOT NULL DEFAULT 10,
	use_proxy boolean NOT NULL DEFAULT false,
	sleep_time integer NOT NULL DEFAULT 2,
	use_session boolean NOT NULL DEFAULT false,
	cookies varchar NULL,
	return_type varchar NOT NULL DEFAULT 'html',
	priority integer NOT NULL DEFAULT 1,
	CONSTRAINT configuration_global_pk PRIMARY KEY (id)
);
CREATE INDEX configuration_start_url_idx ON public.configuration_global (start_url);
CREATE INDEX configuration_spider_name_idx ON public.configuration_global (spider_name);
CREATE INDEX configuration_site_name_idx ON public.configuration_global (site_name);

-- Column comments

COMMENT ON COLUMN public.configuration_global.id IS '主键';
COMMENT ON COLUMN public.configuration_global.start_url IS '入口 URL';
COMMENT ON COLUMN public.configuration_global.spider_name IS '爬虫名称';
COMMENT ON COLUMN public.configuration_global.site_name IS '站点名称';
COMMENT ON COLUMN public.configuration_global.request_method IS '全局请求方式';
COMMENT ON COLUMN public.configuration_global.referer IS '全局referer';
COMMENT ON COLUMN public.configuration_global.need_render IS '是否需要渲染';
COMMENT ON COLUMN public.configuration_global.timeout IS '全局超时时间';
COMMENT ON COLUMN public.configuration_global.use_proxy IS '全局是否需要代理';
COMMENT ON COLUMN public.configuration_global.sleep_time IS '全局最大休眠时间';
COMMENT ON COLUMN public.configuration_global.use_session IS '全局是否需要开启session';
COMMENT ON COLUMN public.configuration_global.cookies IS '全局cookies';
COMMENT ON COLUMN public.configuration_global.return_type IS '全局默认返回网页类型';
COMMENT ON COLUMN public.configuration_global.priority IS '优先级';

-- 请求配置模板表 --

CREATE TABLE public.configuration_request (
	request_id serial NOT NULL,
	start_url varchar NULL,
	request_method varchar NULL DEFAULT 'GET',
	post_data json NULL,
	extra_headers json NULL,
	referer varchar NULL,
	process varchar NULL,
	parameters varchar NULL,
	timeout integer NULL DEFAULT 2,
	sleep_time integer NULL DEFAULT 2,
	need_render boolean NULL DEFAULT false,
	use_proxy boolean NULL DEFAULT false,
	cookies varchar NULL,
	use_session boolean NULL DEFAULT false,
	is_duplicate boolean NULL DEFAULT false,
	"result" varchar NULL,
	return_type varchar NULL,
	return_item varchar NULL,
	stop_by json[] NULL,
	CONSTRAINT configuration_request_pk PRIMARY KEY (request_id)
);

-- Column comments

COMMENT ON COLUMN public.configuration_request.request_id IS '主键';
COMMENT ON COLUMN public.configuration_request.start_url IS '请求 url';
COMMENT ON COLUMN public.configuration_request.request_method IS '请求方式';
COMMENT ON COLUMN public.configuration_request.post_data IS '请求post体';
COMMENT ON COLUMN public.configuration_request.extra_headers IS '额外的请求头';
COMMENT ON COLUMN public.configuration_request.referer IS 'referer';
COMMENT ON COLUMN public.configuration_request.process IS 'process模板，格式process.<数字>';
COMMENT ON COLUMN public.configuration_request.parameters IS '请求 URL 的占位参数';
COMMENT ON COLUMN public.configuration_request.timeout IS '请求超时时间';
COMMENT ON COLUMN public.configuration_request.sleep_time IS '请求休眠时间';
COMMENT ON COLUMN public.configuration_request.need_render IS '请求是否渲染';
COMMENT ON COLUMN public.configuration_request.use_proxy IS '请求是否使用代理';
COMMENT ON COLUMN public.configuration_request.cookies IS 'cookies';
COMMENT ON COLUMN public.configuration_request.use_session IS '是否使用 session 请求';
COMMENT ON COLUMN public.configuration_request.is_duplicate IS '请求是否去重';
COMMENT ON COLUMN public.configuration_request."result" IS '请求的result，格式result.<数字>';
COMMENT ON COLUMN public.configuration_request.return_type IS '请求返回的格式';
COMMENT ON COLUMN public.configuration_request.return_item IS '请求入库的类型，如 Event，即入 event 库';
COMMENT ON COLUMN public.configuration_request.stop_by IS '请求stop条件';

-- 处理配置模板表 --
