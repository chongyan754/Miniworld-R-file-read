-- 输出格式：x:y:z:id

local centerX, centerY, centerZ = 0, 0, 0
local halfRange = 8 
-- 这里指接下来是±8的X,Y,Z 也就是棱长为16的立方体。
for x = centerX - halfRange, centerX + halfRange - 1 do
    for y = centerY - halfRange, centerY + halfRange - 1 do
        for z = centerZ - halfRange, centerZ + halfRange - 1 do
            local result, blockID = Block:getBlockID(x, y, z)
            
            if result == 0 and blockID ~= 0 then
                print(string.format("%d:%d:%d:%d", x, y, z, blockID))
            end
        end
    end
end