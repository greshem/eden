# pygame 函数

# camera (照相机)
    pygame.camera.colorspace()
    pygame.camera.list_cameras()
# cdrom 
    pygame.cdrom.get_count()
    pygame.cdrom.get_init()

# cursors 
    pygame.cursors.compile()
    pygame.cursors.load_xbm()

# display
    pygame.display.Info()  #显示器鑫鑫
    pygame.display.flip()
    pygame.display.get_active()
    pygame.display.get_caption()
    pygame.display.get_driver()
    pygame.display.get_surface()
    pygame.display.get_wm_info()
    pygame.display.gl_get_attribute()
    pygame.display.gl_set_attribute()
    pygame.display.iconify()
    pygame.display.list_modes()
    pygame.display.mode_ok()
    pygame.display.set_caption()
    pygame.display.set_gamma()
    pygame.display.set_gamma_ramp()
    pygame.display.set_icon()
    pygame.display.set_mode()
    pygame.display.set_palette()
    pygame.display.toggle_fullscreen()
    pygame.display.update()

# draw
    pygame.draw.aaline()
    pygame.draw.aalines()
    pygame.draw.arc()       #角
    pygame.draw.circle()    #画圆
    pygame.draw.ellipse()   #椭圆
    pygame.draw.line()      #线段
    pygame.draw.lines()     #线段
    pygame.draw.polygon()   #多边形
    pygame.draw.rect()      #矩形

# encode
    pygame.encode_file_path()
    pygame.encode_string()

# event 
    pygame.event.Event()
    pygame.event.clear()
    pygame.event.event_name()
    pygame.event.get()
    pygame.event.get_blocked()
    pygame.event.get_grab()
    pygame.event.peek()
    pygame.event.poll()
    pygame.event.post()
    pygame.event.pump()
    pygame.event.set_allowed()
    pygame.event.set_blocked()
    pygame.event.set_grab()
    pygame.event.wait()

# examples
    pygame.examples.aliens.main()
    pygame.examples.arraydemo.main()
    pygame.examples.blend_fill.main()
    pygame.examples.blit_blends.main()
    pygame.examples.camera.main()
    pygame.examples.chimp.main()
    pygame.examples.cursors.main()
    pygame.examples.eventlist.main()
    pygame.examples.fastevents.main()
    pygame.examples.fonty.main()
    pygame.examples.freetype_misc.main()
    pygame.examples.glcube.main()
    pygame.examples.headless_no_windows_needed.main()
    pygame.examples.liquid.main()
    pygame.examples.mask.main()
    pygame.examples.midi.main()
    pygame.examples.moveit.main()
    pygame.examples.oldalien.main()
    pygame.examples.overlay.main()
    pygame.examples.pixelarray.main()
    pygame.examples.playmus.main()
    pygame.examples.scaletest.main()
    pygame.examples.scrap_clipboard.main()
    pygame.examples.scroll.main()
    pygame.examples.sound.main()
    pygame.examples.sound_array_demos.main()
    pygame.examples.stars.main()
    pygame.examples.testsprite.main()
    pygame.examples.vgrade.main()

# font 字体
    pygame.font.SysFont()
    pygame.font.get_default_font() #获取默认字体
    pygame.font.get_fonts() #获取字体
    pygame.font.match_font()

# freetype
    pygame.freetype.get_cache_size()
    pygame.freetype.get_default_resolution()
    pygame.freetype.get_version()
    pygame.freetype.set_default_resolution()
    pygame.freetype.was_init()

    pygame.get_error()
    pygame.get_sdl_byteorder()
    pygame.get_sdl_version()

# gfxdraw
    pygame.gfxdraw.aacircle()
    pygame.gfxdraw.aaellipse()
    pygame.gfxdraw.aapolygon()
    pygame.gfxdraw.aatrigon()
    pygame.gfxdraw.bezier()
    pygame.gfxdraw.box()
    pygame.gfxdraw.filled_circle()
    pygame.gfxdraw.filled_ellipse()
    pygame.gfxdraw.filled_polygon()
    pygame.gfxdraw.filled_trigon()
    pygame.gfxdraw.hline()
    pygame.gfxdraw.pie()
    pygame.gfxdraw.pixel()
    pygame.gfxdraw.rectangle()
    pygame.gfxdraw.textured_polygon()
    pygame.gfxdraw.trigon()
    pygame.gfxdraw.vline()

# image 图片
    pygame.image.frombuffer()
    pygame.image.fromstring()
    pygame.image.get_extended()
    pygame.image.load()
    pygame.image.save()
    pygame.image.tostring()

    pygame.init()

# key
    pygame.key.get_focused()
    pygame.key.get_mods()
    pygame.key.get_pressed()
    pygame.key.get_repeat()
    pygame.key.name()
    pygame.key.set_mods()
    pygame.key.set_repeat()

# mask
    pygame.mask.from_surface()
    pygame.mask.from_threshold()
    pygame.math.disable_swizzling()
    pygame.math.enable_swizzling()

# midi
    pygame.midi.MidiException()
    pygame.midi.get_default_input_id()
    pygame.midi.get_default_output_id()
    pygame.midi.get_device_info()
    pygame.midi.midis2events()
    pygame.midi.time()

# mixer 混音器
    pygame.mixer.fadeout()
    pygame.mixer.find_channel()
    pygame.mixer.get_busy()
    pygame.mixer.get_num_channels()
    pygame.mixer.music.get_endevent()
    pygame.mixer.music.get_pos()
    pygame.mixer.music.get_volume()
    pygame.mixer.music.play()
    pygame.mixer.music.queue()
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_endevent()
    pygame.mixer.music.set_pos()
    pygame.mixer.music.set_volume()
    pygame.mixer.pause()
    pygame.mixer.pre_init()
    pygame.mixer.set_num_channels()
    pygame.mixer.set_reserved()
    pygame.mixer.stop()
    pygame.mixer.unpause()

# mouse 鼠标
    pygame.mouse.get_cursor()
    pygame.mouse.get_rel()
    pygame.mouse.set_cursor()
    pygame.mouse.set_visible()

# pixel 像素
    pygame.pixelcopy.array_to_surface()
    pygame.pixelcopy.make_surface()
    pygame.pixelcopy.map_array()
    pygame.pixelcopy.surface_to_array()

    pygame.quit()           #退出
    pygame.register_quit()
    pygame.scrap.contains()
    pygame.scrap.get_types()
    pygame.scrap.lost()
    pygame.scrap.put()
    pygame.set_error()

# sndarray
    pygame.sndarray.array()
    pygame.sndarray.get_arraytype()
    pygame.sndarray.get_arraytypes()
    pygame.sndarray.make_sound()
    pygame.sndarray.samples()
    pygame.sndarray.use_arraytype()

# sprite  精灵
    pygame.sprite.GroupSingle()     #精灵组
    pygame.sprite.OrderedUpdates()  #
    pygame.sprite.collide_circle()  #圆形碰撞检测
    pygame.sprite.collide_circle_ratio()
    pygame.sprite.collide_mask()    
    pygame.sprite.collide_rect()    #矩形检测
    pygame.sprite.collide_rect_ratio()
    pygame.sprite.groupcollide()    #精灵组 碰撞检测
    pygame.sprite.spritecollide()   #碰撞检测
    pygame.sprite.spritecollideany()

# surface 表面 
    pygame.surfarray.array2d()
    pygame.surfarray.array3d()
    pygame.surfarray.array_alpha()
    pygame.surfarray.array_colorkey()
    pygame.surfarray.blit_array()
    pygame.surfarray.pixels2d()
    pygame.surfarray.pixels3d()
    pygame.surfarray.pixels_alpha()
    pygame.surfarray.pixels_blue()
    pygame.surfarray.pixels_green()
    pygame.surfarray.pixels_red()
    pygame.tests.run()
    pygame.time.delay()
    pygame.time.get_ticks()
    pygame.time.set_timer()

#  transform 变形
    pygame.transform.average_color()
    pygame.transform.average_surfaces()
    pygame.transform.chop()
    pygame.transform.get_smoothscale_backend()
    pygame.transform.laplacian()
    pygame.transform.rotate()       #旋转
    pygame.transform.rotozoom()
    pygame.transform.scale()        #放大缩小
    pygame.transform.scale2x()
    pygame.transform.set_smoothscale_backend()
    pygame.transform.smoothscale()
    pygame.transform.threshold()
