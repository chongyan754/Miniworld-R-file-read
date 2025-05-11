asd ={"x5z5.r", "x5z6.r", "x5z7.r", "x5z8.r", "x5z9.r", "x6z5.r", "x6z6.r", "x6z7.r", "x6z8.r", "x6z9.r", "x7z5.r", "x7z6.r", "x7z7.r", "x7z8.r", "x7z9.r", "x8z5.r", "x8z6.r", "x8z7.r", "x8z8.r", "x8z9.r", "x9z5.r", "x9z6.r", "x9z7.r", "x9z8.r", "x9z9.r", }



shi=10


-- 提取坐标的函数，模拟 Python 的 extract_coordinates
function extractCoordinates(s)
    local x, z = s:match("x(%-?%d+)z(%-?%d+)%.r")
    if x and z then
        return tonumber(x), tonumber(z)
    end
    return nil
end

-- 模拟 Python 的 bian 函数，生成坐标列表
function bian(a, b)
    local a_ = a * 32
    local b_ = b * 32
    local x = 0
    local z = 0
    local chu = {}
    
    while z ~= 32 do
        table.insert(chu, {a_, b_})
        x = x + 1
        a_ = a_ + 1
        if x == 32 then
            a_ = a * 32
            b_ = b_ + 1
            z = z + 1
            x = 0
        end
    end
    
    return chu
end

-- 原有的 printChunkBlockIDs 函数
function printChunkBlockIDs(chunkX, chunkZ)
    local baseX = chunkX * 16
    local baseZ = chunkZ * 16
    
    Player:setPosition(0,baseX, 6, baseZ)
    local _, id = Block:getBlockID(baseX, 6, baseZ)
    if id == 100 then
        print("空"..baseX.."/"..baseZ)
        return
    end

    print("实"..baseX.."/"..baseZ)
    for y = 0, 150 do
        local ids = {}

        for dx = 0, 15 do
            for dz = 0, 15 do
                Player:setPosition(0, baseX + dx, y, baseZ + dz)
                local _, id = Block:getBlockID(baseX + dx, y, baseZ + dz)
                table.insert(ids, tostring(id))
            end
        end

        local compressed = ""
        local count = 1
        local prev = ids[1]

        for i = 2, #ids do
            if ids[i] == prev then
                count = count + 1
            else
                compressed = compressed .. count .. "-" .. prev .. "/"
                prev = ids[i]
                count = 1
            end
        end
        compressed = compressed .. count .. "-" .. prev

        print(compressed)
    end
end

-- 主逻辑：处理 asd 列表并调用函数
function main()
    -- 假设 asd 是你提供的输入列表，格式如 {"x26z-1.r", "x27z0.r"}
    
    local filename = asd[1]
    print(filename)
    local x, z = extractCoordinates(filename)
    if x and z then
        local coords = bian(x, z)
        for _, coord in ipairs(coords) do
            printChunkBlockIDs(coord[1], coord[2])
        end
    end
    table.remove(asd, 1) -- 删除已处理的第一个元素
end





function uio()
    shi = shi - 1
    if shi == 0 then  -- Lua用then而不是冒号
        shi = 40
        main()
    end
end

-- 运行主逻辑
ScriptSupportEvent:registerEvent([=[minitimer.change]=],uio)

--printChunkBlockIDs(-5,5)
